import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.004, 0.019).lineTo(-0.004, 0.019).lineTo(-0.004, 0.035).lineTo(0.004, 0.035).lineTo(0.004, 0.019).close()
solid=wp_sketch0.add(loop0).extrude(0.035392793444213436)
