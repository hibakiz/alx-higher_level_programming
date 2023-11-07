#include "lists.h"
/**
*
*
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *node, *new;

	if (head == NULL || *head == NULL)
		return(NULL);
	node = *head;
	prev = node;
	node = node->next;
	if (node->n > number)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = node;
		return(new);
	}
	while (node)
	{
		if (node->n > number)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;
			prev->next = new;
			new->next = node;
			return(new);
		}
		prev = node;
		node = node->next;
	}
	return(NULL);
}
