import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01638, -0.06).lineTo(-0.03188, -0.06).lineTo(-0.03188, -0.05).lineTo(-0.03188, -0.0445).lineTo(-0.00088, -0.0445).lineTo(-0.00088, -0.05).lineTo(-0.00088, -0.06).lineTo(-0.01638, -0.06).close()
solid=wp_sketch0.add(loop0).extrude(0.07647094107927689)
