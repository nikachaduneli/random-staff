<?php
declare(strict_types=1);

class Transaction
{

    private string $name;
    private float $amount;

    public function __construct(string  $name, float $amount)
    {
        $this->amount = $amount;
        $this->name = $name;
    }

}