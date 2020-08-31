#include "lists.h"
#include <stdio.h>
/**
* check_cycle - checks if a sll contains a cycle
* @list: sll
* Return: 0 if there's no cycle, 1 if there's a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *tmp, *head;

	head = list;
	tmp = list;

	while (tmp != NULL && tmp->next != NULL)
	{
		head = head->next;
		tmp = tmp->next->next;
		if (head == tmp)
		{
			return (1);
		}
	}
	return (0);
}
