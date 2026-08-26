# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: SimpleLedger
import copy

def undo_last_action(state):
    """Откат последнего действия: возвращает в состояние до последнего добавления/изменения.
    
    state: dict с ключами:
        categories: list
        counterparties: list
        operations: list
        balance: dict
        history: list of (action_type, entity_id, entity) - история действий
    
    Возвращает: dict с обновлённым состоянием (без истории)
    """
    if not state['history']:
        return state
    
    last_action = state['history'][-1]
    action_type = last_action[0]
    entity_id = last_action[1]
    entity = last_action[2]
    
    if action_type == 'add_category':
        state['categories'].remove(entity)
    elif action_type == 'add_counterparty':
        state['counterparties'].remove(entity)
    elif action_type == 'add_operation':
        state['operations'].remove(entity)
        # Восстанавливаем баланс
        for op in state['operations']:
            if isinstance(op, dict):
                if op.get('amount', 0) == entity.get('amount', 0):
                    balance = {
                        'total': sum(o.get('amount', 0) for o in state['operations']),
                        'by_category': {cat['name']: sum(o.get('amount', 0) for o in state['operations'] if o.get('category', {}).get('name') == cat['name']) for cat in state['categories']},
                        'by_counterparty': {cp['name']: sum(o.get('amount', 0) for o in state['operations'] if o.get('counterparty', {}).get('name') == cp['name']) for cp in state['counterparties']}
                    }
                    state['balance'] = balance
    elif action_type == 'update_category':
        # Обновляем категорию
        state['categories'].remove(entity)
        state['categories'].append(entity)
    elif action_type == 'update_counterparty':
        state['counterparties'].remove(entity)
        state['counterparties'].append(entity)
    elif action_type == 'update_operation':
        # Обновляем операцию
        state['operations'].remove(entity)
        state['operations'].append(entity)
    
    state['history'].pop()
    return state
