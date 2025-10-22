import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.12036, -0.00902).lineTo(-0.02036, -0.00902).lineTo(-0.02036, -0.05902).lineTo(-0.12036, -0.05902).lineTo(-0.12036, -0.00902).close()
solid=wp_sketch0.add(loop0).extrude(0.1589409290210425)
