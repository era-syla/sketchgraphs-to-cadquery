import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.10514, 0.88408).lineTo(-0.09244, 0.88408).lineTo(-0.09244, -0.89392).lineTo(-0.10514, -0.89392).lineTo(-0.10514, 0.88408).close()
solid=wp_sketch0.add(loop0).extrude(0.0655659155466342)
