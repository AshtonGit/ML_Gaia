// Copyright Epic Games, Inc. All Rights Reserved.

#include "ML_EvoSimGameMode.h"
#include "ML_EvoSimPlayerController.h"
#include "ML_EvoSimCharacter.h"
#include "UObject/ConstructorHelpers.h"

AML_EvoSimGameMode::AML_EvoSimGameMode()
{
	// use our custom PlayerController class
	PlayerControllerClass = AML_EvoSimPlayerController::StaticClass();

	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/TopDown/Blueprints/BP_TopDownCharacter"));
	if (PlayerPawnBPClass.Class != nullptr)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}

	// set default controller to our Blueprinted controller
	static ConstructorHelpers::FClassFinder<APlayerController> PlayerControllerBPClass(TEXT("/Game/TopDown/Blueprints/BP_TopDownPlayerController"));
	if(PlayerControllerBPClass.Class != NULL)
	{
		PlayerControllerClass = PlayerControllerBPClass.Class;
	}
}