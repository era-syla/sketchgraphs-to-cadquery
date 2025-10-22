import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02516, -0.06765).lineTo(0.02516, -0.06765).threePointArc((0.03011, -0.06559), (0.03216, -0.06065)).lineTo(0.03216, 0.06065).threePointArc((0.03011, 0.06559), (0.02516, 0.06765)).lineTo(-0.02516, 0.06765).threePointArc((-0.03011, 0.06559), (-0.03216, 0.06065)).lineTo(-0.03216, -0.06065).threePointArc((-0.03011, -0.06559), (-0.02516, -0.06765)).close()
solid=wp_sketch0.add(loop0).extrude(0.006795047143647681)
