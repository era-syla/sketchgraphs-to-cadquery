import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.09338, 0.05595).lineTo(-0.09338, -0.00755).lineTo(0.05695, -0.00444).lineTo(0.05734, -0.02323).lineTo(0.07969, -0.02277).lineTo(0.07884, 0.01837).lineTo(-0.0715, 0.01526).lineTo(-0.07235, 0.0564).lineTo(-0.09338, 0.05595).close()
solid=wp_sketch0.add(loop0).extrude(0.39196993232503297)
