import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.0).lineTo(-0.025, 0.0).lineTo(-0.025, 0.02).threePointArc((-0.01507, 0.00678), (-0.0, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.04322738241645855)
