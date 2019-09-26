Select DISTINCT  A.[AcctDesc] ,L.[UploadDesc], E.[EntDesc], V.* 
from dbo.[Values] V

INNER JOIN dbo.[AccountDetails] A ON A.[AcctID] = V.[AcctID]

INNER JOIN dbo.[Logs] L ON L.[LogID] = V.[LogID]

INNER JOIN dbo.[EntityDetails] E on E.[EntID] = V.[EntID]
