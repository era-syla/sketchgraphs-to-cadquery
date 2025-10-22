import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.06749, 0.07089).lineTo(-0.06656, 0.07089).lineTo(-0.06656, -0.07232).lineTo(0.06749, -0.07232).lineTo(0.06749, 0.07089).close()
solid=wp_sketch0.add(loop0).extrude(0.3178524325487301)
