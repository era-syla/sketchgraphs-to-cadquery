import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.74365, 1.0127).lineTo(0.75635, 1.0127).lineTo(0.75635, 0.9127).lineTo(0.74365, 0.9127).lineTo(0.74365, 1.0127).close()
solid=wp_sketch0.add(loop0).extrude(0.2349222397642048)
