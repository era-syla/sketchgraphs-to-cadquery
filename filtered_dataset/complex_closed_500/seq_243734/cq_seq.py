import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0583, 0.07007).lineTo(0.0687, 0.07007).lineTo(0.0687, 0.0027).threePointArc((0.02226, 0.04776), (-0.02139, 0.0)).lineTo(-0.02139, -0.05693).lineTo(-0.0583, -0.05693).lineTo(-0.0583, 0.07007).close()
solid=wp_sketch0.add(loop0).extrude(0.3582516417315945)
