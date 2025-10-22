import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.08945, -0.02842).lineTo(0.09211, -0.02842).lineTo(0.09211, 0.04033).lineTo(-0.08945, 0.04033).lineTo(-0.08945, -0.02842).close()
solid=wp_sketch0.add(loop0).extrude(0.02785881633123275)
