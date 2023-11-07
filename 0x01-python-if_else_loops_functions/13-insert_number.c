#include "lists.h"
#include<stdio.h>
/**
*
*
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *node, *new;

	node = *head;
	if (node == NULL)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = NULL;
		*head = new;
		return (new);
	}
	prev = node;
	node = node->next;


	if (prev->n > number)
	{
		new = malloc(sizeof(listint_t));
		new->n = number;
		new->next = prev;
		*head = new;
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
	new = malloc(sizeof(listint_t));
	prev->next = new;
	new->n = number;
	new->next = NULL;
	
	return(new);
}
