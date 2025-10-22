import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.012, 0.0).lineTo(0.012, 0.028).lineTo(-0.0, 0.028).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.0031135756809869816)
