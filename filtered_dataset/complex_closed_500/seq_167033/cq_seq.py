import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.2195, 0.165).lineTo(0.2195, 0.165).lineTo(0.2195, -0.165).lineTo(-0.2195, -0.165).lineTo(-0.2195, 0.165).close()
solid=wp_sketch0.add(loop0).extrude(0.9808693175157965)
