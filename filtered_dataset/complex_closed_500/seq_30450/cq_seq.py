import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.12308, 0.02835).lineTo(0.09308, 0.02835).lineTo(0.09308, 0.01335).lineTo(0.12308, 0.01335).lineTo(0.12308, 0.02835).close()
solid=wp_sketch0.add(loop0).extrude(0.030750707391696483)
