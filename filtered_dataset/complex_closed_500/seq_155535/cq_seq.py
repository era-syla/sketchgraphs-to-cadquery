import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.232, 0.295).lineTo(0.232, 0.295).lineTo(0.232, 0.259).lineTo(-0.232, 0.259).lineTo(-0.232, 0.295).close()
solid=wp_sketch0.add(loop0).extrude(0.4402916161424135)
