import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.14, 0.1).lineTo(0.24, 0.1).lineTo(0.24, -0.03).lineTo(-0.14, -0.03).lineTo(-0.14, 0.1).close()
solid=wp_sketch0.add(loop0).extrude(0.6821179109422963)
