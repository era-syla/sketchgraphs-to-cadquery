import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03798, -0.003).lineTo(-0.04198, -0.003).lineTo(-0.04198, 0.003).lineTo(-0.03798, 0.003).lineTo(-0.03798, -0.003).close()
solid=wp_sketch0.add(loop0).extrude(-0.007643875356817023)
