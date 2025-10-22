import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.035, -0.035).lineTo(-0.035, -0.035).lineTo(-0.035, 0.035).lineTo(0.035, 0.035).lineTo(0.035, -0.035).close()
solid=wp_sketch0.add(loop0).extrude(0.11610111818934832)
