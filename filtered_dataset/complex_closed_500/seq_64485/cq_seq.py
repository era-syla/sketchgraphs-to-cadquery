import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.045, 0.11684).lineTo(-0.045, 0.11684).threePointArc((-0.04854, 0.11537), (-0.05, 0.11184)).lineTo(-0.05, 0.10184).threePointArc((-0.04854, 0.0983), (-0.045, 0.09684)).lineTo(0.045, 0.09684).threePointArc((0.04854, 0.0983), (0.05, 0.10184)).lineTo(0.05, 0.11184).threePointArc((0.04854, 0.11537), (0.045, 0.11684)).close()
solid=wp_sketch0.add(loop0).extrude(-0.2267403878337302)
