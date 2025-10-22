import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(1.545, 0.3).threePointArc((1.7175, 0.4725), (1.89, 0.3)).lineTo(1.89, -0.7).lineTo(1.9, -0.7).lineTo(1.9, 0.3).threePointArc((1.7175, 0.4825), (1.535, 0.3)).lineTo(1.535, 0.0).lineTo(1.545, 0.0).lineTo(1.545, 0.3).close()
solid=wp_sketch0.add(loop0).extrude(1.5095755332956187)
