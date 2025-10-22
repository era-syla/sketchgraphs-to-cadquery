import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0625, 0.002).lineTo(-0.0625, 0.002).lineTo(-0.0625, -0.002).lineTo(0.0625, -0.002).lineTo(0.0625, 0.002).close()
solid=wp_sketch0.add(loop0).extrude(0.14096537054571623)
