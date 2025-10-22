import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02041, 0.17817).lineTo(0.02087, 0.17817).lineTo(0.02087, -0.06631).lineTo(-0.02041, -0.06631).lineTo(-0.02041, 0.17817).close()
solid=wp_sketch0.add(loop0).extrude(0.7109774846092299)
