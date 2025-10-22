import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.00454, -0.03807).lineTo(-0.00454, -0.04507).lineTo(0.00396, -0.04307).lineTo(0.00396, -0.03807).lineTo(-0.00454, -0.03807).close()
solid=wp_sketch0.add(loop0).extrude(-0.014987596079375432)
