import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.03602, -0.00538).lineTo(0.04002, -0.00538).lineTo(0.04002, -0.02738).lineTo(0.03602, -0.02738).lineTo(0.03602, -0.00538).close()
solid=wp_sketch0.add(loop0).extrude(-0.005909007494131342)
