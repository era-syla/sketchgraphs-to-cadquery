import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09529, 0.08939).lineTo(-0.19734, 0.08939).lineTo(-0.19734, 0.06397).lineTo(-0.09529, 0.06397).lineTo(-0.09529, 0.08939).close()
solid=wp_sketch0.add(loop0).extrude(-0.11249784048792556)
