import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.07476, 0.07763).lineTo(-0.12242, 0.07763).lineTo(-0.12242, -0.07587).lineTo(-0.07476, -0.07587).lineTo(-0.07476, 0.07763).close()
solid=wp_sketch0.add(loop0).extrude(0.27611873632411016)
