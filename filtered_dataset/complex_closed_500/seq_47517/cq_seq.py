import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.045).lineTo(-0.095, 0.045).lineTo(-0.095, 0.025).threePointArc((-0.08768, 0.00732), (-0.07, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.2786478858296606)
