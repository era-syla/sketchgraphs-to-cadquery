import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.047).lineTo(-0.005, 0.047).lineTo(-0.005, 0.005).lineTo(-0.1, 0.005).lineTo(-0.1, 0.021).lineTo(-0.105, 0.021).lineTo(-0.105, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.17295015856970866)
