import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04, -0.045).lineTo(-0.04, -0.045).threePointArc((-0.04354, -0.04354), (-0.045, -0.04)).lineTo(-0.045, 0.04).threePointArc((-0.04354, 0.04354), (-0.04, 0.045)).lineTo(0.04, 0.045).threePointArc((0.04354, 0.04354), (0.045, 0.04)).lineTo(0.045, -0.04).threePointArc((0.04354, -0.04354), (0.04, -0.045)).close()
solid=wp_sketch0.add(loop0).extrude(-0.10000625494029013)
