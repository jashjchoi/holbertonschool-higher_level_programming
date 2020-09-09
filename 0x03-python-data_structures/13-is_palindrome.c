#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
* is_palindrome - checks if sll is a palindrome
* @head: head of the node
* Return 1 if it's a palindrome, 0 if it's not
*/
int is_palindrome(listint_t **head)
{
	unsigned int length = 1;
	listint_t *tmp;

	if (head == NULL || *head == NULL)
	{
		return (1);
	}
	tmp = *head;
	while (tmp)
	{
		tmp = tmp->next;
		length++;
	}
	return (0);
}
