import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.04998, -0.02236).lineTo(0.60156, -0.02236).lineTo(0.60156, -0.42469).lineTo(0.04998, -0.42469).lineTo(0.04998, -0.02236).close()
solid=wp_sketch0.add(loop0).extrude(0.6729357993862897)
