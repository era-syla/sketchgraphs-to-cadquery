import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05525, 0.05751).lineTo(0.04635, 0.05751).lineTo(0.04635, -0.04409).lineTo(-0.05525, -0.04409).lineTo(-0.05525, 0.05751).close()
solid=wp_sketch0.add(loop0).extrude(0.2336232952429207)
