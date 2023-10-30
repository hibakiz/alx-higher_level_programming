#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks a cycle.
 * @list: linked list.
 *
 * Return: 0 or 1.
  */
int check_cycle(listint_t *list)
{
	listint_t *new, *prev;

	if (list == NULL || list->next == NULL)
		return (0);

	new = list->next;
	prev = list->next->next;

	while (new && prev && prev->next)
	{
		if (new == prev)
			return (1);

		new = new->next;
		prev = prev->next->next;
	}

	return (0);
}
