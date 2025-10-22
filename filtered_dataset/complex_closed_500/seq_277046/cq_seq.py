import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04069, 0.52).lineTo(-0.05069, 0.52).lineTo(-0.05069, 0.51).lineTo(-0.04069, 0.51).lineTo(-0.04069, 0.52).close()
solid=wp_sketch0.add(loop0).extrude(0.011471119054308315)
