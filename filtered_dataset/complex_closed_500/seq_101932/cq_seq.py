import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.02224, 0.08756).lineTo(0.02345, 0.07492).threePointArc((0.02622, 0.07295), (0.02777, 0.07598)).lineTo(0.02301, 0.08775).threePointArc((0.02255, 0.08799), (0.02224, 0.08756)).close()
solid=wp_sketch0.add(loop0).extrude(-0.012975817567417745)
