import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07634, -0.00499).lineTo(-0.07634, 0.03501).lineTo(0.07866, 0.03501).threePointArc((0.11048, 0.02183), (0.12366, -0.00999)).lineTo(0.12366, -0.07499).threePointArc((0.11048, -0.10681), (0.07866, -0.11999)).lineTo(-0.07634, -0.11999).lineTo(-0.07634, -0.07999).lineTo(0.08366, -0.07999).lineTo(0.08366, -0.00499).lineTo(-0.07634, -0.00499).close()
solid=wp_sketch0.add(loop0).extrude(0.10903366774220355)
