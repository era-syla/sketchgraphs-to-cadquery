import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.04389, 0.04083).lineTo(0.04389, 0.04083).threePointArc((0.05096, 0.0379), (0.05389, 0.03083)).lineTo(0.05389, -0.03083).threePointArc((0.05096, -0.0379), (0.04389, -0.04083)).lineTo(-0.04389, -0.04083).threePointArc((-0.05096, -0.0379), (-0.05389, -0.03083)).lineTo(-0.05389, 0.03083).threePointArc((-0.05096, 0.0379), (-0.04389, 0.04083)).close()
solid=wp_sketch0.add(loop0).extrude(0.03819741129587309)
