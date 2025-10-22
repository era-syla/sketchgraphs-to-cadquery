import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.04343, 0.03401).lineTo(0.03843, 0.03401).lineTo(0.03843, 0.04301).lineTo(0.04343, 0.04301).lineTo(0.04343, 0.03401).close()
solid=wp_sketch0.add(loop0).extrude(0.004121134589727295)
