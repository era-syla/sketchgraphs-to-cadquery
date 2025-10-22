import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-2.77483, -3.75).lineTo(2.72517, -3.75).lineTo(2.72517, 3.75).lineTo(-2.77483, 3.75).lineTo(-2.77483, -3.75).close()
solid=wp_sketch0.add(loop0).extrude(13.779961092848247)
