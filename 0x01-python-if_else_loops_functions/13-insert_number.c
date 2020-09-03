#include "lists.h"
/**
* insert_node - inserts a number into a sorted sll
* @head: ptr to the head of sll
* @number: input number
* Return: address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode = malloc(sizeof(listint_t));
	listint_t *prevnode = *head, *nextnode;

	newnode->next = NULL;
	newnode->n = number;

	if (*head == NULL)
	{
		*head = newnode;
		return (newnode);
	}
	nextnode = (*head)->next;
	if (prevnode->n > newnode->n)
	{
		newnode->next = prevnode;
		*head = newnode;
		return (newnode);
	}
	while (nextnode != NULL)
	{
		if (prevnode->n >= newnode->n)
		{
			prevnode->next = newnode;
			newnode->next = nextnode;
			return (newnode);
		}
		prevnode = nextnode;
		nextnode = nextnode->next;
	}
	prevnode->next = newnode;
	return (newnode);
}
