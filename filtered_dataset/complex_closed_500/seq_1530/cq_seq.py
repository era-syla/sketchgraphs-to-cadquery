import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-10.756, 2.585).lineTo(-10.8, 2.585).lineTo(-10.8, 2.732).lineTo(-10.756, 2.732).lineTo(-10.756, 2.585).close()
solid=wp_sketch0.add(loop0).extrude(0.22340379878281694)
