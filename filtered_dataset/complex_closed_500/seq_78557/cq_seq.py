import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05778, -0.00792).lineTo(0.03771, -0.00792).lineTo(0.03771, 0.0651).lineTo(-0.05778, 0.0651).lineTo(-0.05778, -0.00792).close()
solid=wp_sketch0.add(loop0).extrude(0.07316087996256815)
