import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0008, 0.0).lineTo(-0.0008, 0.04).threePointArc((-0.00431, 0.051), (-0.0008, 0.062)).lineTo(0.0005, 0.06107).threePointArc((-0.00271, 0.05075), (0.0008, 0.04052)).lineTo(0.0008, 0.0).lineTo(-0.0008, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.18480562106592954)
