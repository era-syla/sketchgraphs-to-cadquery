import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.07, 0.0025).lineTo(0.07, 0.0025).lineTo(0.07, -0.0025).lineTo(-0.07, -0.0025).lineTo(-0.07, 0.0025).close()
solid=wp_sketch0.add(loop0).extrude(0.3459683762859893)
