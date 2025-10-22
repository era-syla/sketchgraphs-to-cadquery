import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1525, 0.17329).lineTo(0.1144, 0.17329).lineTo(0.1144, 0.16059).lineTo(0.1525, 0.16059).lineTo(0.1525, 0.17329).close()
solid=wp_sketch0.add(loop0).extrude(0.07845780571348672)
