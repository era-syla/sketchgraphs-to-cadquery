import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.14144, 0.06871).lineTo(0.14273, 0.06871).lineTo(0.14273, 0.04371).lineTo(-0.14144, 0.04371).lineTo(-0.14144, 0.06871).close()
solid=wp_sketch0.add(loop0).extrude(-0.07724661513555038)
